grammar Hql;

sql         : SELECT select_stat FROM '(' sql ')' FIELD join_stat '('? sql ')'? FIELD ON cmp_stat group_stat?    # join_sql
            | single_sql                                                                            # derect_sql
            ;

single_sql  : SELECT select_stat FROM FIELD where_stat? group_stat?
            | FIELD
            ;

where_stat  : WHERE cmp_stat (AND cmp_stat)*
            | WHERE cmp_stat (OR cmp_stat)*
            ;
group_stat  : GROUP BY FIELD(','FIELD)*
            ;
join_stat   : LEFT OUTER JOIN
            | FULL OUTER JOIN
            | JOIN
            ;

cmp_stat    : fuction_stat CMP value_stat
            | fuction_stat IS NOT NULL
            | cmp_stat (AND cmp_stat)+
            ;
select_stat : fuction_stat (AS FIELD)?(','fuction_stat (AS FIELD)?)*
            ;
fuction_stat: FIELD'('fuction_stat(','value_stat)*')'
            | if_stat
            | minus_stat
            | FIELD fuction_stat
            | value_stat
            ;
if_stat     : IF'(' cmp_stat',' fuction_stat',' fuction_stat')'
            ;
minus_stat  : FIELD '-' FIELD
            ;
value_stat  : FIELD
            | NUMBERS
            | STRING
            | NULL
            ;

fragment A : [aA];
fragment B : [bB];
fragment C : [cC];
fragment D : [dD];
fragment E : [eE];
fragment F : [fF];
fragment G : [gG];
fragment H : [hH];
fragment I : [iI];
fragment J : [jJ];
fragment K : [kK];
fragment L : [lL];
fragment M : [mM];
fragment N : [nN];
fragment O : [oO];
fragment P : [pP];
fragment Q : [qQ];
fragment R : [rR];
fragment S : [sS];
fragment T : [tT];
fragment U : [uU];
fragment V : [vV];
fragment W : [wW];
fragment X : [xX];
fragment Y : [yY];
fragment Z : [zZ];

SELECT      :   S E L E C T;
FROM        :   F R O M;
WHERE       :   W H E R E;
AND         :   A N D;
OR          :   O R;
GROUP       :   G R O U P;
BY          :   B Y;
AS          :   A S;
IS          :   I S;
NOT         :   N O T;
NULL        :   N U L L;
IF          :   I F;

LEFT        :   L E F T;
FULL        :   F U L L;
OUTER       :   O U T E R;
JOIN        :   J O I N;
ON          :   O N;

FIELD       :   CHARS('.'CHARS)?
            ;
//TABLE       :   CHARS('.'CHARS)?
//            ;
NUMBERS     :   [0-9]+;
STRING      :   '\'' .+? '\'';
CHARS       :   [a-zA-Z_]+;
CMP         :   '='
            |   '<>'
            |   '>'
            |   '>='
            |   '<'
            |   '<='
            ;

WS: [ \r\t\n]+ -> skip;