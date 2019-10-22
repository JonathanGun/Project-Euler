program euler;
uses udate;

var
	d, i, ans : longint;
begin
	d := 2; ans := 0;
	for i := DateToDays(StrToDate('01/01/1901')) to DateToDays(StrToDate('31/12/2000')) do begin
		// if (DaysToDate(i).day = 1) then begin writeln(DateToStr(DaysToDate(i)), ' ', d, ' ', ans); readln(); end;
		if (DaysToDate(i).day = 1) and (d = 0) then ans += 1;
		d := (d + 1) mod 7;
	end;
	writeln(ans);
end.