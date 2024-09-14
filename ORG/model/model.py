class BaseModel:
    def add(self, args):
        if not args:
            raise ValueError("输入不能为空")
        self.table.insert(args)

    def list(self):
        return self.table.all()

    def get_by_id(self, idx):
        return self.table.get(doc_id=idx) or {}
