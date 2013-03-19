//newline ::= .

funtion_definition ::= function_header NEWLINE function_body.
function_header ::= DEF SOMETHING_NEW LEFT_PARENTHESIS optional_args RIGHT_PARENTHESIS COLON.
function_body ::= statements END.

optional_args ::= .
optional_args ::= arg.
optional_args ::= optional_args arg.
arg ::= SOMETHING_NEW.

//*how will that be handled in the editor?*

statements ::= statement.
statements ::= statements statement.

statement ::= while_loop.
while_loop ::= WHILE expression DO statements END.

expression ::= statement.

