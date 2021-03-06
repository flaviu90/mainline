class PipelineStep():
    def __init__(self):
        self.items = []

    def read(self):
        raise NotImplementedError()

    def process_item(self, item):
        raise NotImplementedError()

    def run(self):
        items = self.read()
        items_to_write = []
        cnt = 0
        for item in items:
            try:
                print "Processing page %d" % cnt
                cnt += 1
                processed_items = self.process_item(item)
                items_to_write.extend(processed_items)
            except:
                self.log_fail(item)
        print len(items_to_write)
        self.write(items_to_write)

    def log_fail(self, item):
        #TODO: log item
        pass

    def write(self, item):
        raise NotImplementedError() 
