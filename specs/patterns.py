import zodchy
import hermitage


class ReadInvoice(hermitage.notation.Invoice):
    def __init__(self, *elements: hermitage.notation.Bucket):
        super().__init__(
            *map(lambda b: b + hermitage.notation.Clause("deleted_at", zodchy.operators.IS(None)), elements)
        )


class WriteInvoice(hermitage.notation.Invoice):
    pass
