class Evaluator:
    def zip_evaluate(coefs, words):
        result = 0
        if len(coefs) != len(words):
            return -1
        for pair in zip(coefs, words):
            result += pair[0] * len(pair[1])
        return result

    def enumerate_evaluate(coefs, words):
        result = 0
        if len(coefs) != len(words):
            return -1
        for i, val in enumerate(coefs):
            result += val * len(words[i])
        return result


if __name__ == '__main__':
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]

    print("# Zip")
    print(Evaluator.zip_evaluate(coefs, words))
    print("# Enumerate")
    print(Evaluator.enumerate_evaluate(coefs, words))
    print()

    print("--different length--")

    words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
    coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]

    print("# Zip")
    print(Evaluator.zip_evaluate(coefs, words))
    print("# Enumerate")
    print(Evaluator.enumerate_evaluate(coefs, words))

    print("--------------------------------")

    words = ["Le"]
    coefs = [1.0]

    print("# Zip")
    print(Evaluator.zip_evaluate(coefs, words))
    print("# Enumerate")
    print(Evaluator.enumerate_evaluate(coefs, words))

    print("--------------------------------")

    words = ["Le", "el"]
    coefs = [3.0, 0.0]

    print("# Zip")
    print(Evaluator.zip_evaluate(coefs, words))
    print("# Enumerate")
    print(Evaluator.enumerate_evaluate(coefs, words))
