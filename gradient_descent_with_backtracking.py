import tensorflow as tf

class GragientDescentWithBackTracking:
    def __init__(self, x, f, df,):
        """
        Args:
            x: tensorflow variable of shape `[batch_len, n]`
            f: tensor of shape `[batch_len]`            
            
        """
        floatX = f.dtype
        
        self.x = x
        self.f = f
        self.df = df
        
        # define vars we need
        
        self.x_c = tf.Variable(x, name = "x_c", dtype = floatX, validate_shape=False)
        self.x_c.set_shape([None, None])
    
        self.f_c = tf.Variable(f, name = "f_c", dtype = floatX, validate_shape=False)
        self.f_c.set_shape([None])
    
        self.df_c = tf.Variable(x, name = "df_c", dtype = floatX, validate_shape=False)
        self.df_c.set_shape([None, None])
    
        self.x_p = tf.Variable(x, name = "x_p", dtype = floatX, validate_shape=False)
        self.x_p.set_shape([None, None])
    
        self.f_p = tf.Variable(f, name = "f_p", dtype = floatX, validate_shape=False)
        self.f_p.set_shape([None])
    
        self.df_p = tf.Variable(x, name = "df_p", dtype = floatX, validate_shape=False)
        self.df_p.set_shape([None, None])
    
        self.condition = tf.Variable(tf.ones_like(f, dtype = bool), name = "condition", dtype = tf.bool, validate_shape=False)
        self.condition.set_shape([None])
    
        self.alpha = tf.Variable(tf.ones_like(f), name = "alpha", dtype = floatX, validate_shape=False)
        self.alpha.set_shape([None])
        
    def construct_initializer(
        self, 
        initial_step_length = 5,
        minimal_grad_length = 1e-5,
    ):
        """Return initializer which sets such alpha to get specified step length.
        
        Namely alpha is set by the formula:
            `alpha = initial_step_length / max(minimal_grad_length, norm(df))`        
        
        Args:
            initial_step_length: scalar. Step length we want to achieve.
            minimal_grad_length: scalar
            
        """
        return tf.group(
            *[
                tf.assign(
                    var, val, name = name + "_initializer", 
                    validate_shape=False
                )
                for var, val, name in [
                    [self.x_c, self.x, "x_c"],
                    [self.f_c, self.f, "f_c"],
                    [self.df_c, self.df, "df_c"],
        
                    [self.x_p, self.x, "x_p"],
                    [self.f_p, self.f, "f_p"],
                    [self.df_p, self.df, "df_p"],        
                ]
            ], 
            tf.assign(
                self.alpha,
                initial_step_length / tf.maximum(minimal_grad_length, tf.norm(self.df, axis = -1)),
                name = "alpha_initializer", 
                validate_shape = False
            ),
            tf.assign(
                self.condition, tf.cast(tf.ones_like(self.f), tf.bool), 
                validate_shape=False),
            name = "initialization"
        )
        
        
    def construct_step_sequence(self, c1 = 0.5, rho =  0.5):
        """
        Args:
            c1 = sufficient_descent_const = 0.5
            rho = step_contraction_factor = 0.5
        """
        x = self.x
        x_c = self.x_c
        x_p = self.x_p
        
        f = self.f
        f_c = self.f_c
        f_p = self.f_p
        
        df = self.df
        df_c = self.df_c
        df_p = self.df_p
        
        alpha = self.alpha
        condition = self.condition
        
        
        ### Step 1
        ## $$x_p := x_c - \alpha\cdot df_c$$
        s1 = tf.assign(x_p, x_c - alpha[:, None] * df_c)
        
        ### Step 2 and 3
        ## $$f_p := f(x_p)$$
        ## $$df_p := df(x_p)$$
        
        s2 = tf.assign(x, x_p + 1 - 1)
        s3 = tf.group(
            tf.assign(f_p, f + 1 - 1, name = "evaluate_f_p"),
            tf.assign(df_p, df + 1 - 1, name = "evaluate_df_p")
        )
        
        ### Step 4 and 5
        ## Sufficient descent condition is:
        ## $$f_p \leq f_c + c_1 (x_p - x_c)\cdot df_c $$
        ## If it is satisfied then:
        ## $$x_c := x_p; \quad f_c := f_p; \quad df_c := df_p; \quad \alpha := \alpha; \quad  $$
        ## otherwise
        ## $$x_c := x_c; \quad f_c := f_c; \quad df_c := df_c; \quad \alpha := \rho\cdot \alpha; \quad  $$
        
        s4 = tf.assign(
            condition,
            f_p <= f_c + c1 * tf.einsum("bi,bi->b", x_p - x_c, df_c),
            name = "evaluate_condition",
            validate_shape = True,
        )
        
        condition2 = tf.cast(
            tf.cast(condition[:, None], tf.int32) * tf.ones_like(x, tf.int32),
            bool
        )

        s5 = tf.group(
                tf.assign(x_c, tf.where(condition2, x_p, x_c)),
                tf.assign(f_c, tf.where(condition, f_p, f_c)),
                tf.assign(df_c, tf.where(condition2, df_p, df_c)),
                tf.assign(alpha, tf.where(condition, alpha, rho * alpha)),
            )
        
        s6 = tf.assign(x, x_c)
        
        return [s1, s2, s3, s4, s5, s6]
        
      