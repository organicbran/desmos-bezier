// changes colors of all desmos lines at once
// paste this into browser console (inspect -> console)
state = Calc.getState();
for (i = 0; i < state.expressions.list.length; i++)
{
    state.expressions.list[i].color="#000000"
    // default line width is 2.5
    state.expressions.list[i].lineWidth="4"
    // default line opacity is 0.9
    state.expressions.list[i].lineOpacity="1"
}
Calc.setState(state);