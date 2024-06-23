from asyncflows import Action, BaseModel, Field

class Inputs(BaseModel):
    input_string: str
    word_index: int = Field(
        description="Index of the word to reverse (0-based)",
        default=0
    )

class Outputs(BaseModel):
    reversed_string: str

class MyReverseString(Action[Inputs, Outputs]):
    name = 'my_reverse_string'

    async def run(self, inputs: Inputs) -> Outputs:
        words = inputs.input_string.split()
        if inputs.word_index < len(words):
            words[inputs.word_index] = words[inputs.word_index][::-1]
        return Outputs(
            reversed_string=' '.join(words)
        )