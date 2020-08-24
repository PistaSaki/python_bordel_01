from sacred import Experiment

ex = Experiment("my_experiment")

@ex.automain
def main():
    print("running")
    try:
        0 / 0
    except Exception as exc:
        new_exc = Exception("Problem in the caclulation.")
        raise new_exc from exc
