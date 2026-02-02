/*
 * LEX File for Expression & Conditional Parser
 * Purpose: Tokenize arithmetic expressions and conditional statements
 * Supports: if-else, arithmetic operators, relational operators
 */

%{
#include "parser.tab.h"
#include <stdio.h>
#include <stdlib.h>

extern int line_num;
%}

%option noyywrap

%%

"if"		{ return IF; }
"else"		{ return ELSE; }

[a-zA-Z_][a-zA-Z0-9_]*		{ return ID; }
[0-9]+		{ yylval = atoi(yytext); return NUM; }

">="		{ return GE; }
"<="		{ return LE; }
"=="		{ return EQ; }
"!="		{ return NE; }

"&&"		{ return AND; }
"||"		{ return OR; }
"!"		{ return NOT; }

">"		{ return '>'; }
"<"		{ return '<'; }

"+"		{ return '+'; }
"-"		{ return '-'; }
"*"		{ return '*'; }
"/"		{ return '/'; }
"%"		{ return '%'; }

"="		{ return '='; }

"("		{ return '('; }
")"		{ return ')'; }
"{"		{ return '{'; }
"}"		{ return '}'; }
";"		{ return ';'; }

"?"		{ return '?'; }
":"		{ return ':'; }

[ \t\r]+	{ /* ignore whitespace and carriage returns */ }
\n		{ line_num++; }

"//".*		{ /* ignore single-line comments */ }

.		{ 
		fprintf(stderr, "Lexical Error: Invalid character '%c' at line %d\n", 
			yytext[0], line_num);
		return yytext[0];
	}

%%

