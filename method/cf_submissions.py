
# from quickchart import QuickChart
import pickle

class Cf_submissions:
    def __init__(self, data):
        self.data = data

    def getRatioTags(self):
        data = {}
        total = 0
        for submission in self.data:
            if submission["verdict"] != "OK":
                continue

            for tag in submission["problem"]["tags"]:
                total += 1
                if tag in data.keys():
                    data[tag] += 1
                else:
                    data[tag] = 1

        # for tag, val in data.items():
        #     data[tag] = val/total

        return data

    def visualizeRatioTags(self, ratio):
        tags = []
        vals = []
        for tag, val in ratio.items():
            tags.append(tag)
            vals.append(val)
        print(tag)
        print()
        print(val)
        print()
        data = {
            "type": "pie",
            "data": {
                "labels": tags,
                "datasets": [
                    {
                        "data": vals,
                        "label": "Dataset 1"
                    }
                ]
            }
        }
        
        # print(pickle.dumps(data).encode('base64', 'strict'))
        return data