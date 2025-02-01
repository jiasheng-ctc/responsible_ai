import sys
import os

# Ensure the application can find the guardrails module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
from guardrails_utils.guardrails_validation import validate_sensitive_profanity_and_pii, validate_sql, is_sql_statement

# Dash App setup
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = 'Guardrail Chatbot Demo'

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H2("Guardrail Chatbot", className="text-center my-3"), width=12)
    ]),
    
    dbc.Row([
        dbc.Col(
            dbc.Card([
                dbc.CardBody([
                    dcc.Textarea(
                        id='user-input',
                        placeholder='Type your message...',
                        style={'width': '100%', 'height': '120px', 'resize': 'none'}
                    ),
                    html.Br(),
                    dbc.Button("Send", id='submit-button', color="primary", className="w-100 mt-2"),
                    html.Div(id="loading-spinner", children=[], className="mt-2"),
                    html.Div(id='validation-result', className="mt-3 text-center")
                ])
            ]), width=10
        )
    ], justify="center"),
], fluid=True)

@app.callback(
    [Output('validation-result', 'children'),
     Output('validation-result', 'className'),
     Output('loading-spinner', 'children')],
    Input('submit-button', 'n_clicks'),
    State('user-input', 'value')
)
def validate_input(n_clicks, user_input):
    if not user_input:
        return "⚠️ Please enter a message.", "alert alert-warning", []

    # Show loading spinner
    loading_spinner = dbc.Spinner(size="sm", color="primary")

    if is_sql_statement(user_input):
        sql_validation_result = validate_sql(user_input)
        if 'SQL Validation failed' in sql_validation_result:
            return f"❌ {sql_validation_result}", "alert alert-danger", []
    else:
        validation_result = validate_sensitive_profanity_and_pii(user_input)
        if 'Validation failed' in validation_result:
            return f"❌ {validation_result}", "alert alert-danger", []

    return "✅ Message is safe to proceed.", "alert alert-success", []

if __name__ == '__main__':
    app.run_server(debug=True)
