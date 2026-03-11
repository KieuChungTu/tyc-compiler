"""
Lexer test cases for TyC compiler
TODO: Implement 100 test cases for lexer
"""

import pytest
from tests.utils import Tokenizer


# ========== Simple Test Cases (10 types) ==========
def test_keyword_auto():
    """1. Keyword"""
    tokenizer = Tokenizer("auto")
    assert tokenizer.get_tokens_as_string() == "auto,<EOF>"


def test_operator_assign():
    """2. Operator"""
    tokenizer = Tokenizer("=")
    assert tokenizer.get_tokens_as_string() == "=,<EOF>"


def test_separator_semi():
    """3. Separator"""
    tokenizer = Tokenizer(";")
    assert tokenizer.get_tokens_as_string() == ";,<EOF>"


def test_integer_single_digit():
    """4. Integer literal"""
    tokenizer = Tokenizer("5")
    assert tokenizer.get_tokens_as_string() == "5,<EOF>"


def test_float_decimal():
    """5. Float literal"""
    tokenizer = Tokenizer("3.14")
    assert tokenizer.get_tokens_as_string() == "3.14,<EOF>"


def test_string_simple():
    """6. String literal"""
    tokenizer = Tokenizer('"hello"')
    assert tokenizer.get_tokens_as_string() == "hello,<EOF>"


def test_identifier_simple():
    """7. Identifier"""
    tokenizer = Tokenizer("x")
    assert tokenizer.get_tokens_as_string() == "x,<EOF>"


def test_line_comment():
    """8. Line comment"""
    tokenizer = Tokenizer("// This is a comment")
    assert tokenizer.get_tokens_as_string() == "<EOF>"


def test_integer_in_expression():
    """9. Mixed: integers and operator"""
    tokenizer = Tokenizer("5+10")
    assert tokenizer.get_tokens_as_string() == "5,+,10,<EOF>"


def test_complex_expression():
    """10. Complex: variable declaration"""
    tokenizer = Tokenizer("auto x = 5 + 3 * 2;")
    assert tokenizer.get_tokens_as_string() == "auto,x,=,5,+,3,*,2,;,<EOF>"

# ========== KEYWORDS (16) ==========

def test_001_keyword_auto():
    tokenizer = Tokenizer("auto")
    assert tokenizer.get_tokens_as_string() == "auto,<EOF>"

def test_002_keyword_int():
    tokenizer = Tokenizer("int")
    assert tokenizer.get_tokens_as_string() == "int,<EOF>"

def test_003_keyword_float():
    tokenizer = Tokenizer("float")
    assert tokenizer.get_tokens_as_string() == "float,<EOF>"

def test_004_keyword_string():
    tokenizer = Tokenizer("string")
    assert tokenizer.get_tokens_as_string() == "string,<EOF>"

def test_005_keyword_struct():
    tokenizer = Tokenizer("struct")
    assert tokenizer.get_tokens_as_string() == "struct,<EOF>"

def test_006_keyword_void():
    tokenizer = Tokenizer("void")
    assert tokenizer.get_tokens_as_string() == "void,<EOF>"

def test_007_keyword_if():
    tokenizer = Tokenizer("if")
    assert tokenizer.get_tokens_as_string() == "if,<EOF>"

def test_008_keyword_else():
    tokenizer = Tokenizer("else")
    assert tokenizer.get_tokens_as_string() == "else,<EOF>"

def test_009_keyword_for():
    tokenizer = Tokenizer("for")
    assert tokenizer.get_tokens_as_string() == "for,<EOF>"

def test_010_keyword_while():
    tokenizer = Tokenizer("while")
    assert tokenizer.get_tokens_as_string() == "while,<EOF>"

def test_011_keyword_switch():
    tokenizer = Tokenizer("switch")
    assert tokenizer.get_tokens_as_string() == "switch,<EOF>"

def test_012_keyword_case():
    tokenizer = Tokenizer("case")
    assert tokenizer.get_tokens_as_string() == "case,<EOF>"

def test_013_keyword_default():
    tokenizer = Tokenizer("default")
    assert tokenizer.get_tokens_as_string() == "default,<EOF>"

def test_014_keyword_break():
    tokenizer = Tokenizer("break")
    assert tokenizer.get_tokens_as_string() == "break,<EOF>"

def test_015_keyword_continue():
    tokenizer = Tokenizer("continue")
    assert tokenizer.get_tokens_as_string() == "continue,<EOF>"

def test_016_keyword_return():
    tokenizer = Tokenizer("return")
    assert tokenizer.get_tokens_as_string() == "return,<EOF>"


# ========== OPERATORS + SEPARATORS (22) ==========

def test_017_operator_assign():
    tokenizer = Tokenizer("=")
    assert tokenizer.get_tokens_as_string() == "=,<EOF>"

def test_018_operator_plus():
    tokenizer = Tokenizer("+")
    assert tokenizer.get_tokens_as_string() == "+,<EOF>"

def test_019_operator_minus():
    tokenizer = Tokenizer("-")
    assert tokenizer.get_tokens_as_string() == "-,<EOF>"

def test_020_operator_mul():
    tokenizer = Tokenizer("*")
    assert tokenizer.get_tokens_as_string() == "*,<EOF>"

def test_021_operator_div():
    tokenizer = Tokenizer("/")
    assert tokenizer.get_tokens_as_string() == "/,<EOF>"

def test_022_operator_mod():
    tokenizer = Tokenizer("%")
    assert tokenizer.get_tokens_as_string() == "%,<EOF>"

def test_023_operator_eq():
    tokenizer = Tokenizer("==")
    assert tokenizer.get_tokens_as_string() == "==,<EOF>"

def test_024_operator_neq():
    tokenizer = Tokenizer("!=")
    assert tokenizer.get_tokens_as_string() == "!=,<EOF>"

def test_025_operator_lt():
    tokenizer = Tokenizer("<")
    assert tokenizer.get_tokens_as_string() == "<,<EOF>"

def test_026_operator_lte():
    tokenizer = Tokenizer("<=")
    assert tokenizer.get_tokens_as_string() == "<=,<EOF>"

def test_027_operator_gt():
    tokenizer = Tokenizer(">")
    assert tokenizer.get_tokens_as_string() == ">,<EOF>"

def test_028_operator_gte():
    tokenizer = Tokenizer(">=")
    assert tokenizer.get_tokens_as_string() == ">=,<EOF>"

def test_029_operator_or():
    tokenizer = Tokenizer("||")
    assert tokenizer.get_tokens_as_string() == "||,<EOF>"

def test_030_operator_and():
    tokenizer = Tokenizer("&&")
    assert tokenizer.get_tokens_as_string() == "&&,<EOF>"

def test_031_operator_not():
    tokenizer = Tokenizer("!")
    assert tokenizer.get_tokens_as_string() == "!,<EOF>"

def test_032_operator_inc():
    tokenizer = Tokenizer("++")
    assert tokenizer.get_tokens_as_string() == "++,<EOF>"

def test_033_operator_dec():
    tokenizer = Tokenizer("--")
    assert tokenizer.get_tokens_as_string() == "--,<EOF>"

def test_034_operator_dot():
    tokenizer = Tokenizer(".")
    assert tokenizer.get_tokens_as_string() == ".,<EOF>"

def test_035_separator_braces():
    tokenizer = Tokenizer("{}")
    assert tokenizer.get_tokens_as_string() == "{,},<EOF>"

def test_036_separator_parens():
    tokenizer = Tokenizer("()")
    assert tokenizer.get_tokens_as_string() == "(,),<EOF>"

def test_037_separator_semi():
    tokenizer = Tokenizer(";")
    assert tokenizer.get_tokens_as_string() == ";,<EOF>"

def test_038_separator_mixed_no_comma_token():
    tokenizer = Tokenizer("({});:")
    assert tokenizer.get_tokens_as_string() == "(,{,},),;,:,<EOF>"


# ========== IDENTIFIERS (10) ==========

def test_039_identifier_simple():
    tokenizer = Tokenizer("x")
    assert tokenizer.get_tokens_as_string() == "x,<EOF>"

def test_040_identifier_underscore_start():
    tokenizer = Tokenizer("_x")
    assert tokenizer.get_tokens_as_string() == "_x,<EOF>"

def test_041_identifier_with_digits():
    tokenizer = Tokenizer("var123")
    assert tokenizer.get_tokens_as_string() == "var123,<EOF>"

def test_042_identifier_keyword_prefix():
    tokenizer = Tokenizer("auto1")
    assert tokenizer.get_tokens_as_string() == "auto1,<EOF>"

def test_043_identifier_keyword_suffix():
    tokenizer = Tokenizer("intVar")
    assert tokenizer.get_tokens_as_string() == "intVar,<EOF>"

def test_044_identifier_mixed_case():
    tokenizer = Tokenizer("Point3D")
    assert tokenizer.get_tokens_as_string() == "Point3D,<EOF>"

def test_045_identifier_many_underscores():
    tokenizer = Tokenizer("__a__b__")
    assert tokenizer.get_tokens_as_string() == "__a__b__,<EOF>"

def test_046_identifier_long():
    s = "a" * 50
    tokenizer = Tokenizer(s)
    assert tokenizer.get_tokens_as_string() == f"{s},<EOF>"

def test_047_identifier_two_ids():
    tokenizer = Tokenizer("x y")
    assert tokenizer.get_tokens_as_string() == "x,y,<EOF>"

def test_048_identifier_not_keyword_structs():
    tokenizer = Tokenizer("structs")
    assert tokenizer.get_tokens_as_string() == "structs,<EOF>"


# ========== NUMBERS (16) ==========

def test_049_int_zero():
    tokenizer = Tokenizer("0")
    assert tokenizer.get_tokens_as_string() == "0,<EOF>"

def test_050_int_leading_zeros():
    tokenizer = Tokenizer("00012")
    assert tokenizer.get_tokens_as_string() == "00012,<EOF>"

def test_051_float_standard():
    tokenizer = Tokenizer("3.14")
    assert tokenizer.get_tokens_as_string() == "3.14,<EOF>"

def test_052_float_trailing_dot():
    tokenizer = Tokenizer("1.")
    assert tokenizer.get_tokens_as_string() == "1.,<EOF>"

def test_053_float_leading_dot():
    tokenizer = Tokenizer(".5")
    assert tokenizer.get_tokens_as_string() == ".5,<EOF>"

def test_054_float_exponent():
    tokenizer = Tokenizer("1e10")
    assert tokenizer.get_tokens_as_string() == "1e10,<EOF>"

def test_055_float_exponent_sign():
    tokenizer = Tokenizer("2.5e-3")
    assert tokenizer.get_tokens_as_string() == "2.5e-3,<EOF>"

def test_056_int_in_expression():
    tokenizer = Tokenizer("5+10")
    assert tokenizer.get_tokens_as_string() == "5,+,10,<EOF>"

def test_057_negative_int_standalone():
    tokenizer = Tokenizer("-45")
    assert tokenizer.get_tokens_as_string() == "-,45,<EOF>"

def test_058_negative_int_after_assign():
    tokenizer = Tokenizer("auto x=-12;")
    assert tokenizer.get_tokens_as_string() == "auto,x,=,-,12,;,<EOF>"

def test_059_negative_int_in_parens():
    tokenizer = Tokenizer("(-10)")
    assert tokenizer.get_tokens_as_string() == "(,-,10,),<EOF>"

def test_060_negative_int_after_mul():
    tokenizer = Tokenizer("a*-5")
    assert tokenizer.get_tokens_as_string() == "a,*,-,5,<EOF>"

def test_061_subtraction_not_negative_literal():
    tokenizer = Tokenizer("5-10")
    assert tokenizer.get_tokens_as_string() == "5,-,10,<EOF>"

def test_062_case_negative_int_context():
    tokenizer = Tokenizer("case -1:")
    assert tokenizer.get_tokens_as_string() == "case,-,1,:,<EOF>"

def test_063_return_negative_int_context():
    tokenizer = Tokenizer("return -10;")
    assert tokenizer.get_tokens_as_string() == "return,-,10,;,<EOF>"

def test_064_dot_vs_float_ambiguity():
    tokenizer = Tokenizer("1..2")
    assert tokenizer.get_tokens_as_string() == "1.,.2,<EOF>"


# ========== STRINGS (20) ==========

def test_065_string_simple():
    tokenizer = Tokenizer('"hello"')
    assert tokenizer.get_tokens_as_string() == "hello,<EOF>"

def test_066_string_empty():
    tokenizer = Tokenizer('""')
    assert tokenizer.get_tokens_as_string() == ",<EOF>"

def test_067_string_with_spaces():
    tokenizer = Tokenizer('"hello world"')
    assert tokenizer.get_tokens_as_string() == "hello world,<EOF>"

def test_068_string_with_symbols():
    tokenizer = Tokenizer('"a1_+=-"')
    assert tokenizer.get_tokens_as_string() == "a1_+=-,<EOF>"

def test_069_string_contains_comment_markers():
    tokenizer = Tokenizer('"//not comment/*still string*/"')
    assert tokenizer.get_tokens_as_string() == "//not comment/*still string*/,<EOF>"

def test_070_string_escape_n():
    tokenizer = Tokenizer('"a\\n"')
    assert tokenizer.get_tokens_as_string() == "a\\n,<EOF>"

def test_071_string_escape_t():
    tokenizer = Tokenizer('"a\\t"')
    assert tokenizer.get_tokens_as_string() == "a\\t,<EOF>"

def test_072_string_backslashes():
    tokenizer = Tokenizer('"\\\\"')
    assert tokenizer.get_tokens_as_string() == "\\\\,<EOF>"

def test_073_string_escape_quote():
    tokenizer = Tokenizer('"\\""')
    assert tokenizer.get_tokens_as_string() == '\\",<EOF>'

def test_074_string_multiple_escapes():
    tokenizer = Tokenizer('"a\\n\\t\\\\b"')
    assert tokenizer.get_tokens_as_string() == "a\\n\\t\\\\b,<EOF>"

def test_075_string_with_braces_parens():
    tokenizer = Tokenizer('"{( )}"')
    assert tokenizer.get_tokens_as_string() == "{( )},<EOF>"

def test_076_string_adjacent_identifier():
    tokenizer = Tokenizer('"hi"x')
    assert tokenizer.get_tokens_as_string() == "hi,x,<EOF>"

def test_077_string_plus_string():
    tokenizer = Tokenizer('"a"+"b"')
    assert tokenizer.get_tokens_as_string() == "a,+,b,<EOF>"

def test_078_string_in_call_args():
    tokenizer = Tokenizer('f("a","b");')
    assert tokenizer.get_tokens_as_string() == "f,(,a,,,b,),;,<EOF>"

def test_079_string_illegal_escape_q():
    tokenizer = Tokenizer('"ab\\qcd"')
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: ab\\q"

def test_080_string_illegal_escape_a():
    tokenizer = Tokenizer('"x\\a"')
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: x\\a"

def test_081_string_illegal_escape_at_eof():
    tokenizer = Tokenizer('"ab\\q')
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: ab\\q"

def test_082_string_unclosed_eof():
    tokenizer = Tokenizer('"abc')
    assert tokenizer.get_tokens_as_string() == "Unclosed String: abc"

def test_083_string_unclosed_newline():
    tokenizer = Tokenizer("\"abc\n")
    assert tokenizer.get_tokens_as_string() == "Unclosed String: abc"

def test_084_string_unclosed_crlf():
    tokenizer = Tokenizer("\"abc\r\n")
    assert tokenizer.get_tokens_as_string() == "Unclosed String: abc"


# ========== COMMENTS / WHITESPACE (8) ==========

def test_085_line_comment_only():
    tokenizer = Tokenizer("// This is a comment")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_086_line_comment_after_code():
    tokenizer = Tokenizer("x//comment")
    assert tokenizer.get_tokens_as_string() == "x,<EOF>"

def test_087_line_comment_then_newline_then_code():
    tokenizer = Tokenizer("x//c\ny")
    assert tokenizer.get_tokens_as_string() == "x,y,<EOF>"

def test_088_block_comment_only():
    tokenizer = Tokenizer("/* comment */")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_089_block_comment_between_ids():
    tokenizer = Tokenizer("a/*c*/b")
    assert tokenizer.get_tokens_as_string() == "a,b,<EOF>"

def test_090_block_comment_with_symbols_inside():
    tokenizer = Tokenizer("a/* + - * / % == */b")
    assert tokenizer.get_tokens_as_string() == "a,b,<EOF>"

def test_091_whitespace_tabs_newlines():
    tokenizer = Tokenizer(" \t\n auto \r\n x ")
    assert tokenizer.get_tokens_as_string() == "auto,x,<EOF>"

def test_092_many_newlines():
    tokenizer = Tokenizer("\n\n\nint\nx\n;\n")
    assert tokenizer.get_tokens_as_string() == "int,x,;,<EOF>"


# ========== MIXED + ERROR TOKENS (8) ==========

def test_093_struct_declaration_tokens():
    tokenizer = Tokenizer("struct Point{int x,y;};")
    assert tokenizer.get_tokens_as_string() == "struct,Point,{,int,x,,,y,;,},;,<EOF>"

def test_094_function_declaration_tokens():
    tokenizer = Tokenizer("int f(int x){return x;}")
    assert tokenizer.get_tokens_as_string() == "int,f,(,int,x,),{,return,x,;,},<EOF>"

def test_095_if_else_tokens():
    tokenizer = Tokenizer("if(x) y=1; else y=2;")
    assert tokenizer.get_tokens_as_string() == "if,(,x,),y,=,1,;,else,y,=,2,;,<EOF>"

def test_096_for_loop_tokens():
    tokenizer = Tokenizer("for(i=0;i<3;i++){}")
    assert tokenizer.get_tokens_as_string() == "for,(,i,=,0,;,i,<,3,;,i,++,),{,},<EOF>"

def test_097_switch_case_default_tokens():
    tokenizer = Tokenizer("switch(x){case -1: return 0; default: return 1;}")
    assert tokenizer.get_tokens_as_string() == (
        "switch,(,x,),{,case,-,1,:,return,0,;,default,:,return,1,;,},<EOF>"
    )
    
def test_098_complex_expression_tokens():
    tokenizer = Tokenizer("auto x=5+3*2==11&&y!=0;")
    assert tokenizer.get_tokens_as_string() == "auto,x,=,5,+,3,*,2,==,11,&&,y,!=,0,;,<EOF>"

def test_099_error_token_single():
    tokenizer = Tokenizer("@")
    assert tokenizer.get_tokens_as_string() == "Error Token @"

def test_100_error_token_after_valid_tokens():
    tokenizer = Tokenizer("auto x = 1; #")
    assert tokenizer.get_tokens_as_string() == "auto,x,=,1,;,Error Token #"
