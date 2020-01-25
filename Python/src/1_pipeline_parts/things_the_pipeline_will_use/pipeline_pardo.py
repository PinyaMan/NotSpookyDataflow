import apache_beam


class WordSplitCustomPardo(apache_beam.DoFn):
    def process(self, element: str):
        input_data = element
        output_data = element.split()

        print("Hi from WordSplitCustomPardo: \n\tINPUT: ", input_data, "\n\tOUTPUT: ", output_data)
        return output_data


class DataPrinterCustomPardo(apache_beam.DoFn):
    def process(self, element: str):
        input_data = element
        output_data = element

        print("Hi from DataPrinterCustomPardo (☞ﾟ∀ﾟ)☞: \n\tINPUT: ", input_data, "\n\tOUTPUT: ", output_data)
        return output_data
