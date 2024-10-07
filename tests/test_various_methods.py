import unittest
import numpy as np
import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from ..src.various_methods import ModelWrapper

class TestModelWrapper(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        This runs once for the entire test case. Load the Iris dataset and prepare the test model.
        """
        # Load the Iris dataset for testing
        cls.iris_data = load_iris()
        cls.X_test = cls.iris_data.data[:20]  # Test with first 20 samples
        
        # Save a test model (LogisticRegression) if not already saved
        cls.model_path = 'test_model.pkl'
        cls.model = LogisticRegression(max_iter=200)
        cls.model.fit(cls.iris_data.data, cls.iris_data.target)
        joblib.dump(cls.model, cls.model_path)
        
        # Create a second test model to simulate reloading
        cls.new_model_path = 'new_test_model.pkl'
        cls.new_model = LogisticRegression(max_iter=200)
        cls.new_model.fit(cls.iris_data.data, cls.iris_data.target)
        joblib.dump(cls.new_model, cls.new_model_path)

    def test_model_loading(self):
        """
        Test if the model is correctly loaded from the file.
        """
        model_wrapper = ModelWrapper(self.model_path)
        
        # Check if the model has been loaded correctly
        self.assertIsNotNone(model_wrapper.model, "Model should be loaded and not None")
        self.assertIsInstance(model_wrapper.model, LogisticRegression, "Loaded model should be an instance of LogisticRegression")

    def test_predictions(self):
        """
        Test if the predict function gives the correct shape of output.
        """
        model_wrapper = ModelWrapper(self.model_path)
        predictions = model_wrapper.predict(self.X_test)

        # Check if predictions are not empty
        self.assertIsNotNone(predictions, "Predictions should not be None")

        # Check if the number of predictions matches the number of input samples
        self.assertEqual(predictions.shape[0], self.X_test.shape[0], "Number of predictions should match the number of input samples")

    def test_invalid_input(self):
        """
        Test how the model handles invalid input.
        """
        model_wrapper = ModelWrapper(self.model_path)

        # Provide an input that doesn't match the expected feature dimensions
        invalid_input = np.array([[1, 2, 3, 4, 5]])  # Should have 20 features instead of 5
        with self.assertRaises(ValueError):
            model_wrapper.predict(invalid_input)

    def test_reload_model_simulation(self):
        """
        Test if the model can be reloaded by reinitializing the ModelWrapper with a new path.
        """
        # Initialize the wrapper with the first model
        model_wrapper = ModelWrapper(self.__class__.model_path)

        # Check that the model is loaded correctly
        self.assertIsNotNone(model_wrapper.model, "Model should be loaded and not None")
        self.assertIsInstance(model_wrapper.model, LogisticRegression, "Model should be an instance of LogisticRegression")

        # Reinitialize the wrapper with the new model path (simulate reloading)
        model_wrapper = ModelWrapper(self.__class__.new_model_path)

        # Check that the model is reloaded with the new path
        self.assertIsNotNone(model_wrapper.model, "Model should be reloaded and not None")
        self.assertIsInstance(model_wrapper.model, LogisticRegression, "Reloaded model should be an instance of LogisticRegression")

    @classmethod
    def tearDownClass(cls):
        # Cleanup: remove test files if necessary
        import os
        os.remove(cls.model_path)
        os.remove(cls.new_model_path)

if __name__ == '__main__':
    unittest.main()