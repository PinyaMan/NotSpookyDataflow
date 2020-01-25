import apache_beam as beam


class UniqueWordsParDo(beam.DoFn):
    """
    ParDo is a Beam transform for generic parallel processing. A ParDo transform considers each element in the input
    PCollection, performs some processing function (your user code) on that element, and emits zero, one, or multiple
    elements to an output PCollection.
    """

    def process(self, element: str, *args, **kwargs):
        """

        :param element: It will be a sentence and we will emit a list of unic words, within the same sentence.
        :param args:
        :param kwargs:
        :return:
        Input 1: ["The cake is a cake"] Output 1: ["The","cake","is","a"]
        Input 2: ["Tasty cake"] Output 2: ["Tasty", "cake"]
        """
        splitted_words_list = element.split()
        aux_list = []

        return [word for word in splitted_words_list if word not in aux_list]


class SimpleMapPardo(beam.DoFn):
    def process(self, element: list, *args, **kwargs):
        """
        Emits a key value pair for each element in the input collection
        """
        return [(i, 1) for i in element]


class PrinterParDo(beam.DoFn):
    def process(self, element, *args, **kwargs):
        print(element)
        return element


class SimpleReducePardo(beam.DoFn):
    def process(self, element: tuple, *args, **kwargs):
        """
        Emits a key value pair for each element in the input collection
        """
        print("SIMPLE REDUCE", element)
        return element
        key, value = element
        accumulate = 0
        for i in value:
            accumulate += i
        return key, accumulate
