# python-OOP-Lec6-04-JUN-25
Recursion: presentation 31

* Recursion is a function that calls for itself.
* usage:
  * This technique provides a way to break complicated problems down into simple problems which are easier to solve.
* till reach stopping condition and then return back till the first caller and exist.
  * usually:
    1) we put first the stopping condition and the return back
    2) call the function with the change
    3) if the function needs to return a value: 
       1. use return foo()
       2. use return in the stopping condition
    4) else just call foo()