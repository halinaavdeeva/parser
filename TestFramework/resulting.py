

class Result:
    def __init__(self, folder):
        if folder == 'books_data_table':
            self.result_file = open('results/books_data_table.log', 'w')
        else:
            self.result_file = open('results/flowers_for_alegron_table.log', 'w')

    def start_test(self, folder):
        self.result_file.write('\n\nTesting of {} was started\n'.format(folder))

    def finish_test(self):
        self.result_file.close()

    def start_case(self, test_name):
        self.result_file.write("\n\nTest case '{}'".format(test_name))

    def add_pass(self, query, actual_result):
        self.result_file.write("\nPASS. Result is '{0}' as expected"
                               "\n\tQuery: {1}".format(actual_result, query))

    def add_fail(self, query, actual_result, expected_result):
        self.result_file.write("\nFAIL. Result is '{0}', but expected '{1}'"
                               "\n\tQuery: {2}".format(actual_result, expected_result, query))