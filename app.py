"""
Production Grade Version using OOP
"""
def main():
    from wrapper import FlaskWrapper
    run_server = FlaskWrapper()
    run_server(debug=True, port=1234)

if __name__ == "__main__":
    main()