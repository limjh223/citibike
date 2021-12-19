from dash import dcc, html
from conclusion_blurbs import conclusion_blurb, next_steps_blurb

conclusion_tab = dcc.Tab(
    label = 'Conclusion',
    value = 'conclusion',
    children = [html.H2('Conclusions'),
                html.Div(conclusion_blurb),
                html.H2('Next Steps'),
                html.Div(next_steps_blurb)])