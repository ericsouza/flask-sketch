from PyInquirer import Token, style_from_dict


cli_style = style_from_dict(
    {
        Token.QuestionMark: "#E91E63 bold",
        Token.Selected: "#673AB7 bold",
        Token.Instruction: "",
        Token.Answer: "#2196f3 bold",
        Token.Question: "",
    }
)


cli_style_2 = style_from_dict(
    {
        Token.Separator: "#6C6C6C",
        Token.Questionmark: "#FF9D00 bold",
        Token.Selected: "#5F819D",
        Token.Pointer: "#FF9D00 bold",
        Token.Instruction: "",
        Token.Answer: "#5F819D bold",
        Token.Question: "",
    }
)
