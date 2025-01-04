import logging
import tests_12_1 as r
import unittest

logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log",
                    encoding="utf-8", format="%(asctime)s -|- %(levelname)s -|- %(message)s")


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner_1 = r.Runner('Вася', -5)
            for _ in range(10):
                runner_1.walk()
            self.assertEqual(runner_1.distance, 100)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    def test_run(self):
        try:
            runner_2 = r.Runner(5)
            for _ in range(10):
                runner_2.run()
            self.assertEqual(runner_2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    if __name__ == "__main__":
        unittest.main()