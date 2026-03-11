"""
Parser test cases for TyC compiler
TODO: Implement 100 test cases for parser
"""

import pytest
from tests.utils import Parser


# ========== Simple Test Cases (10 types) ==========
def test_empty_program():
    """1. Empty program"""
    assert Parser("").parse() == "success"


def test_program_with_only_main():
    """2. Program with only main function"""
    assert Parser("void main() {}").parse() == "success"


def test_struct_simple():
    """3. Struct declaration"""
    source = "struct Point { int x; int y; };"
    assert Parser(source).parse() == "success"


def test_function_no_params():
    """4. Function with no parameters"""
    source = "void greet() { printString(\"Hello\"); }"
    assert Parser(source).parse() == "success"


def test_var_decl_auto_with_init():
    """5. Variable declaration"""
    source = "void main() { auto x = 5; }"
    assert Parser(source).parse() == "success"


def test_if_simple():
    """6. If statement"""
    source = "void main() { if (1) printInt(1); }"
    assert Parser(source).parse() == "success"


def test_while_simple():
    """7. While statement"""
    source = "void main() { while (1) printInt(1); }"
    assert Parser(source).parse() == "success"


def test_for_simple():
    """8. For statement"""
    source = "void main() { for (auto i = 0; i < 10; ++i) printInt(i); }"
    assert Parser(source).parse() == "success"


def test_switch_simple():
    """9. Switch statement"""
    source = "void main() { switch (1) { case 1: printInt(1); break; } }"
    assert Parser(source).parse() == "success"


def test_assignment_simple():
    """10. Assignment statement"""
    source = "void main() { int x; x = 5; }"
    assert Parser(source).parse() == "success"


# ============================================================
#  PARSER TEST SUITE (100 cases)
#  - success cases: assert ... == "success"
#  - error cases:   assert ... != "success"  (error text may vary)
# ============================================================

# ========== 001–010: Program + top-level declarations ==========

def test_001_empty_program():
    assert Parser("").parse() == "success"

def test_002_only_void_main():
    assert Parser("void main() {}").parse() == "success"

def test_003_only_main_no_ret_type():
    assert Parser("main() {}").parse() == "success"

def test_004_two_functions():
    src = "void a() {} int b() { return 1; }"
    assert Parser(src).parse() == "success"

def test_005_struct_only():
    src = "struct Point { int x; int y; };"
    assert Parser(src).parse() == "success"

def test_006_struct_then_function():
    src = "struct P { int x; }; void main() { }"
    assert Parser(src).parse() == "success"

def test_007_multiple_structs():
    src = "struct A { int x; }; struct B { float y; string s; };"
    assert Parser(src).parse() == "success"

def test_008_mixed_decl_order():
    src = "void f() {} struct S { int a; }; void g() {}"
    assert Parser(src).parse() == "success"

def test_009_struct_empty_members_ok():
    src = "struct Empty { };"
    assert Parser(src).parse() == "success"

def test_010_struct_missing_trailing_semi_error():
    src = "struct A { int x; }"
    assert Parser(src).parse() != "success"


# ========== 011–020: Function headers + parameters ==========

def test_011_func_no_params_return_int():
    src = "int f() { return 1; }"
    assert Parser(src).parse() == "success"

def test_012_func_with_params_primitive():
    src = "int add(int a, int b) { return a + b; }"
    assert Parser(src).parse() == "success"

def test_013_func_with_params_mixed_types():
    src = "void log(int a, float b, string c) { return; }"
    assert Parser(src).parse() == "success"

def test_014_func_no_ret_type_with_params():
    src = "sum(int a, int b) { return a + b; }"
    assert Parser(src).parse() == "success"

def test_015_func_return_struct_type():
    src = "struct P { int x; }; P make() { return {1}; }"
    assert Parser(src).parse() == "success"

def test_016_func_param_struct_type():
    src = "struct P { int x; }; int g(P p) { return 1; }"
    assert Parser(src).parse() == "success"

def test_017_param_trailing_comma_error():
    src = "int f(int a, ) { return a; }"
    assert Parser(src).parse() != "success"

def test_018_missing_param_name_error():
    src = "int f(int) { return 1; }"
    assert Parser(src).parse() != "success"

def test_019_missing_rparen_error():
    src = "int f(int a { return a; }"
    assert Parser(src).parse() != "success"

def test_020_function_prototype_not_allowed_error():
    src = "void f();"
    assert Parser(src).parse() != "success"


# ========== 021–030: Struct members + var declarations ==========

def test_021_struct_members_id_list():
    src = "struct T { int a,b,c; float x; string s; };"
    assert Parser(src).parse() == "success"

def test_022_struct_member_missing_semi_error():
    src = "struct T { int a };"  # missing ';' after member
    assert Parser(src).parse() != "success"

def test_023_local_var_decl_single():
    src = "void main() { int x; }"
    assert Parser(src).parse() == "success"

def test_024_local_var_decl_multiple():
    src = "void main() { int a,b,c; }"
    assert Parser(src).parse() == "success"

def test_025_local_var_decl_init():
    src = "void main() { int x=1; }"
    assert Parser(src).parse() == "success"

def test_026_local_var_decl_multi_init():
    src = "void main() { int a=1,b=2,c=3; }"
    assert Parser(src).parse() == "success"

def test_027_auto_var_decl_init():
    src = "void main() { auto x = 10; }"
    assert Parser(src).parse() == "success"

def test_028_auto_var_decl_no_init_ok_by_grammar():
    src = "void main() { auto x; }"
    assert Parser(src).parse() == "success"

def test_029_var_decl_missing_name_error():
    src = "void main() { int ; }"
    assert Parser(src).parse() != "success"

def test_030_var_decl_missing_semi_error():
    src = "void main() { int x }"
    assert Parser(src).parse() != "success"


# ========== 031–040: Blocks + statement mixing ==========

def test_031_nested_blocks():
    src = "void main() { { { int x; } } }"
    assert Parser(src).parse() == "success"

def test_032_empty_statements():
    src = "void main() { ; ; ; }"
    assert Parser(src).parse() == "success"

def test_033_block_items_mix():
    src = "void main() { int x; x=1; ; return; }"
    assert Parser(src).parse() == "success"

def test_034_stmt_then_var_decl_still_ok_by_grammar():
    src = "void main() { x=1; int y; y=2; }"
    assert Parser(src).parse() == "success"

def test_035_missing_rbrace_error():
    src = "void main() { int x; "
    assert Parser(src).parse() != "success"

def test_036_extra_rbrace_error():
    src = "void main() { } }"
    assert Parser(src).parse() != "success"

def test_037_global_var_decl_not_allowed_error():
    src = "int x;"
    assert Parser(src).parse() != "success"

def test_038_struct_inside_block_not_allowed_error():
    src = "void main() { struct A { int x; }; }"
    assert Parser(src).parse() != "success"

def test_039_return_missing_semi_error():
    src = "void main() { return }"
    assert Parser(src).parse() != "success"

def test_040_expr_missing_semi_error():
    src = "void main() { x=1 }"
    assert Parser(src).parse() != "success"


# ========== 041–050: If / else ==========

def test_041_if_simple():
    src = "void main() { if(1) printInt(1); }"
    assert Parser(src).parse() == "success"

def test_042_if_else_simple():
    src = "void main() { if(1) x=1; else x=2; }"
    assert Parser(src).parse() == "success"

def test_043_nested_if_else():
    src = "void main() { if(1) if(0) x=1; else x=2; }"
    assert Parser(src).parse() == "success"

def test_044_if_block_body():
    src = "void main() { if(1) { int x; x=1; } }"
    assert Parser(src).parse() == "success"

def test_045_if_else_block_body():
    src = "void main() { if(1){x=1;} else {x=2;} }"
    assert Parser(src).parse() == "success"

def test_046_if_missing_parens_error():
    src = "void main() { if 1 x=1; }"
    assert Parser(src).parse() != "success"

def test_047_else_without_if_error():
    src = "void main() { else x=1; }"
    assert Parser(src).parse() != "success"

def test_048_if_missing_stmt_error():
    src = "void main() { if(1) }"
    assert Parser(src).parse() != "success"

def test_049_if_condition_complex_precedence():
    src = "void main() { if(1+2*3==7&&0||1) ; }"
    assert Parser(src).parse() == "success"

def test_050_if_missing_rparen_error():
    src = "void main() { if(1 { x=1; } }"
    assert Parser(src).parse() != "success"


# ========== 051–060: While / For ==========

def test_051_while_simple():
    src = "void main() { while(1) x=1; }"
    assert Parser(src).parse() == "success"

def test_052_while_block():
    src = "void main() { while(x) { x=x-1; } }"
    assert Parser(src).parse() == "success"

def test_053_while_missing_parens_error():
    src = "void main() { while 1 x=1; }"
    assert Parser(src).parse() != "success"

def test_054_for_all_parts_present():
    src = "void main() { for(i=0; i<10; i=i+1) ; }"
    assert Parser(src).parse() == "success"

def test_055_for_missing_init_ok():
    src = "void main() { for(; i<10; i=i+1) ; }"
    assert Parser(src).parse() == "success"

def test_056_for_missing_cond_ok():
    src = "void main() { for(i=0; ; i=i+1) ; }"
    assert Parser(src).parse() == "success"

def test_057_for_missing_update_ok():
    src = "void main() { for(i=0; i<10; ) ; }"
    assert Parser(src).parse() == "success"

def test_058_for_all_missing_ok():
    src = "void main() { for(;;) ; }"
    assert Parser(src).parse() == "success"

def test_059_for_with_var_decl_init():
    src = "void main() { for(int i=0; i<10; i=i+1) ; }"
    assert Parser(src).parse() == "success"

def test_060_for_missing_semicolons_error():
    src = "void main() { for(i=0 i<10 i=i+1) ; }"
    assert Parser(src).parse() != "success"


# ========== 061–070: Switch / case / default ==========

def test_061_switch_single_case():
    src = "void main() { switch(x){ case 1: x=2; } }"
    assert Parser(src).parse() == "success"

def test_062_switch_case_break():
    src = "void main() { switch(x){ case 1: x=2; break; } }"
    assert Parser(src).parse() == "success"

def test_063_switch_multiple_cases():
    src = "void main() { switch(x){ case 1: x=1; case 2: x=2; } }"
    assert Parser(src).parse() == "success"

def test_064_switch_default_only():
    src = "void main() { switch(x){ default: x=0; } }"
    assert Parser(src).parse() == "success"

def test_065_switch_case_default_mix():
    src = "void main() { switch(x){ case 1: x=1; default: x=0; } }"
    assert Parser(src).parse() == "success"

def test_066_switch_case_negative_expr():
    src = "void main() { switch(x){ case -1: return; } }"
    assert Parser(src).parse() == "success"

def test_067_switch_missing_colon_error():
    src = "void main() { switch(x){ case 1 x=1; } }"
    assert Parser(src).parse() != "success"

def test_068_switch_missing_brace_error():
    src = "void main() { switch(x) case 1: x=1; }"
    assert Parser(src).parse() != "success"

def test_069_switch_nested_switch():
    src = "void main() { switch(x){ case 1: switch(y){default: y=0;} } }"
    assert Parser(src).parse() == "success"

def test_070_switch_case_missing_expr_error():
    src = "void main() { switch(x){ case : x=1; } }"
    assert Parser(src).parse() != "success"


# ========== 071–080: Return / break / continue / expr statements ==========

def test_071_return_no_expr():
    src = "void main(){ return; }"
    assert Parser(src).parse() == "success"

def test_072_return_with_expr():
    src = "int main(){ return 1+2*3; }"
    assert Parser(src).parse() == "success"

def test_073_break_stmt_parses():
    src = "void main(){ break; }"
    assert Parser(src).parse() == "success"

def test_074_continue_stmt_parses():
    src = "void main(){ continue; }"
    assert Parser(src).parse() == "success"

def test_075_call_stmt():
    src = "void main(){ printInt(1); }"
    assert Parser(src).parse() == "success"

def test_076_member_access_chain_stmt():
    src = "void main(){ a.b.c; }"
    assert Parser(src).parse() == "success"

def test_077_call_chain_stmt():
    src = "void main(){ a.b(1,2).c(3); }"
    assert Parser(src).parse() == "success"

def test_078_post_inc_stmt():
    src = "void main(){ i++; }"
    assert Parser(src).parse() == "success"

def test_079_prefix_inc_stmt():
    src = "void main(){ ++i; }"
    assert Parser(src).parse() == "success"

def test_080_continue_missing_semi_error():
    src = "void main(){ continue }"
    assert Parser(src).parse() != "success"


# ========== 081–090: Expression precedence / associativity ==========

def test_081_assign_right_associative():
    src = "void main(){ a=b=c=1; }"
    assert Parser(src).parse() == "success"

def test_082_or_and_precedence():
    src = "void main(){ x = a || b && c; }"
    assert Parser(src).parse() == "success"

def test_083_eq_rel_mix():
    src = "void main(){ x = a < b == c != d; }"
    assert Parser(src).parse() == "success"

def test_084_add_mul_mod_precedence():
    src = "void main(){ x = 1 + 2 * 3 - 4 / 2 % 2; }"
    assert Parser(src).parse() == "success"

def test_085_unary_not_chain():
    src = "void main(){ x = !!!1; }"
    assert Parser(src).parse() == "success"

def test_086_unary_minus_float():
    src = "void main(){ x = -3.14; }"
    assert Parser(src).parse() == "success"

def test_087_prefix_and_postfix_mix():
    src = "void main(){ x = ++i + j--; }"
    assert Parser(src).parse() == "success"

def test_088_nested_calls_and_parens():
    src = "void main(){ f(1+2, g(3*4), (5)); }"
    assert Parser(src).parse() == "success"

def test_089_dot_and_call_precedence():
    src = "void main(){ x = a.b(1).c + d.e; }"
    assert Parser(src).parse() == "success"

def test_090_assign_with_unary_and_logic():
    src = "void main(){ x = -(1+2) * 3 > 0 && !y; }"
    assert Parser(src).parse() == "success"


# ========== 091–100: Struct literals + hard syntax errors ==========

def test_091_struct_literal_empty_exprstmt():
    src = "void main(){ {}; }"
    assert Parser(src).parse() == "success"

def test_092_struct_literal_list():
    src = "void main(){ x = {1,2,3}; }"
    assert Parser(src).parse() == "success"

def test_093_struct_literal_nested():
    src = "void main(){ x = { {1}, {2,3} }; }"
    assert Parser(src).parse() == "success"

def test_094_struct_literal_in_call():
    src = "void main(){ f({1,2}); }"
    assert Parser(src).parse() == "success"

def test_095_args_trailing_comma_error():
    src = "void main(){ f(1,2,); }"
    assert Parser(src).parse() != "success"

def test_096_missing_comma_between_args_error():
    src = "void main(){ f(1 2); }"
    assert Parser(src).parse() != "success"

def test_097_two_literals_adjacent_error():
    # lexer can tokenize 1..2 as 1. and .2, but parser should reject adjacency
    src = "void main(){ x = 1..2; }"
    assert Parser(src).parse() != "success"

def test_098_incomplete_expression_error():
    src = "void main(){ x = 1 + ; }"
    assert Parser(src).parse() != "success"

def test_099_unbalanced_parens_error():
    src = "void main(){ x = (1+2; }"
    assert Parser(src).parse() != "success"

def test_100_missing_block_in_function_error():
    src = "void main()"
    assert Parser(src).parse() != "success"
