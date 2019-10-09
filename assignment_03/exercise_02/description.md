In this task, you will perform some basic data science on a small dataset containing information about dogs in the city of Zurich. You are given a csv file with the raw data and have to implement some functions that help you answer statistical questions about the data.


Start by familiarizing yourself with the dataset. Look at the csv and then read through the code and the documentation. The function that reads the csv is already implemented for you. The functions without implementation should have enough details in the docstring to help you write the missing code. To check if your code is working you can try running the code but keep in mind that you also have the tests to check if your code is working as expected. You can also create a toy dataset with the same format, but only a few lines, so that you can manually check whether your functions work correctly.
You can execute single tests from the suite, through PyCharm or by running, for example, `python3 task_2_test.py Task2Test.test_preview_dognames -v -b` from the command line.

*Note:* We provided you with only a sample from the original dataset, and will use the whole set or another sample of it to test your implementation, as well as a more complete test suite.
Task: Fill in the missing function implementations of the following functions:

* `preview_dognames`
* `dognames_count`
* `top_n_dognames`
* `is_valid_row`
* `filter_dognames`