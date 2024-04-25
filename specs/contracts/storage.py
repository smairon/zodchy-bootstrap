import hermitage
import hermitage_alchemy

EngineContract = hermitage_alchemy.AsyncEngineContract
WriteConnectionContract = hermitage_alchemy.WriteAsyncConnectionContract
ReadConnectionContract = hermitage_alchemy.ReadAsyncConnectionContract
ReadClientContract = hermitage_alchemy.ReadClientContract
WriteClientContract = hermitage_alchemy.WriteClientContract


class ReadInvoice(hermitage.Invoice):
    def __init__(
        self,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self._elements.append(hermitage.Clause("deleted_at", hermitage.query.IS(None)))
        self._distribute_elements()


class WriteInvoice(hermitage.Invoice):
    pass
