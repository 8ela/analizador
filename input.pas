<<<<<<< HEAD
PROGRAM Sort(input, output);
    CONST
        MaxElts = 50;
    TYPE
        IntArrType = ARRAY [1..MaxElts] OF Integer;

    VAR
        i, j, tmp, size: integer;
        arr: IntArrType;

    PROCEDURE ReadArr(VAR size: Integer; VAR a: IntArrType);
        BEGIN
            size := 1;
            WHILE NOT eof DO BEGIN
                readln(a[size]);
                IF NOT eof THEN
                    size := size + 1
            END
        END;

    BEGIN
        ReadArr(size, arr);

        FOR i := size - 1 DOWNTO 1 DO
            FOR j := 1 TO i DO
                IF arr[j] > arr[j + 1] THEN BEGIN
                    tmp := arr[j];
                    arr[j] := arr[j + 1];
                    arr[j + 1] := tmp;
                END;

        FOR i := 1 TO size DO
            writeln(arr[i])
    END.
=======
function max(num1, num2: integer): integer;

var
   result: integer;

begin
   if (num1 > num2) then
      result := num1
   
   else
      result := num2;
   max := result;
end;
>>>>>>> e97dc5cf3e3124deff5c78d090ff2dff983fba04
