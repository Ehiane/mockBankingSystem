# Banking System

This project is a basic banking system that allows users to manage and access their accounts. It provides functionality for login, account creation, verification of user information, and distribution of account balances. The system includes loading animations and utilizes the `User` and `Bank` classes for efficient data manipulation.

## Key Features

- **User Authentication**: Existing users can log in by providing their name and the last four digits of their routing number. This ensures secure access to their accounts.
- **Account Creation**: New users can create their accounts by entering their personal details. The system verifies the information before displaying their account balances.
- **Balance Management**: Users can deposit and withdraw funds from their accounts, and the system updates the balances accordingly. The program includes methods for depositing, withdrawing, and viewing account balances.
- **Account Distribution**: Users can distribute their balance among multiple accounts. The system supports a maximum of two accounts per user.
- **Data Storage**: User information is stored in a dictionary, where the user's name serves as the key, and the routing and account numbers are stored as values. This allows for efficient retrieval and manipulation of user data.
- **Loading Animations**: The program includes loading animations that display messages while executing various tasks. This enhances the user experience and provides feedback during processing.

## Getting Started

To use the banking system, follow these steps:

1. Clone the repository to your local machine.
2. Ensure you have Python installed (version 3.0 or higher).
3. Run the `banking_system.py` file in a Python IDE or terminal.
4. Follow the on-screen prompts to either log in as an existing user or create a new user account.
5. Use the provided options to manage your accounts, deposit/withdraw funds, and view balances.

## Technology Stack

The banking system is developed using the following technologies and concepts:

- **Python**: The programming language used for system development.
- **Object-Oriented Programming**: The system is structured around the `User` and `Bank` classes, enabling efficient data management and code organization.
- **Random and String Modules**: These modules are utilized to generate random routing and account numbers.
- **User Interface**: The system provides a command-line interface for user interaction. Users can input their choices and receive prompt messages and account information.

## Future Enhancements

The current version of the banking system provides a solid foundation for account management. However, there are several areas that can be further improved:

- **Additional Account Types**: Extend the system to support more account types, such as savings, credit, or investment accounts.
- **Security Enhancements**: Implement advanced security measures, such as password authentication and encryption, to ensure the safety of user data.
- **GUI Implementation**: Develop a graphical user interface (GUI) to enhance the user experience and make the system more visually appealing.
- **Database Integration**: Integrate the system with a database to enable persistent data storage and retrieval, allowing users to access their accounts across multiple sessions.

## Contributing

Contributions to the banking system project are welcome. If you have any ideas, bug fixes, or enhancements, feel free to open an issue or submit a pull request. Your contributions will be greatly appreciated.

## Acknowledgments

This project was a collaboration between [Ehiane Oigiagbe](https://github.com/ehiane) and [Chat-GPT](https://chat.openai.com/). Their combined efforts and expertise resulted in the successful development of this basic banking system.

## License

This project is licensed under the [MIT License](LICENSE). You are free to modify and use the codebase
