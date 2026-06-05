import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class TicTacToe extends JFrame implements ActionListener {
    private JButton[] buttons = new JButton[9];
    private boolean isPlayerX = true; // True for X, false for O
    private JLabel statusLabel;

    public TicTacToe() {
        setTitle("Tic Tac Toe");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(400, 450);
        setLayout(new BorderLayout());

        // Create game board
        JPanel board = new JPanel();
        board.setLayout(new GridLayout(3, 3));
        for (int i = 0; i < 9; i++) {
            buttons[i] = new JButton("");
            buttons[i].setFont(new Font("Arial", Font.BOLD, 60));
            buttons[i].addActionListener(this);
            board.add(buttons[i]);
        }

        // Status label
        statusLabel = new JLabel("Player X's Turn");
        statusLabel.setHorizontalAlignment(SwingConstants.CENTER);
        statusLabel.setFont(new Font("Arial", Font.BOLD, 16));

        // Add components
        add(statusLabel, BorderLayout.NORTH);
        add(board, BorderLayout.CENTER);

        setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        JButton clickedButton = (JButton) e.getSource();

        // Set the button text to X or O if not already clicked
        if (clickedButton.getText().equals("")) {
            clickedButton.setText(isPlayerX ? "X" : "O");
            clickedButton.setEnabled(false);

            // Check for a winner
            if (checkWinner()) {
                statusLabel.setText("Player " + (isPlayerX ? "X" : "O") + " Wins!");
                disableAllButtons();
                return;
            }

            // Check for a draw
            if (isDraw()) {
                statusLabel.setText("It's a Draw!");
                return;
            }

            // Switch player turn
            isPlayerX = !isPlayerX;
            statusLabel.setText("Player " + (isPlayerX ? "X" : "O") + "'s Turn");
        }
    }

    private boolean checkWinner() {
        // Possible winning combinations
        int[][] winCombinations = {
            {0, 1, 2}, {3, 4, 5}, {6, 7, 8}, // Rows
            {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, // Columns
            {0, 4, 8}, {2, 4, 6}             // Diagonals
        };

        for (int[] combo : winCombinations) {
            if (!buttons[combo[0]].getText().equals("") &&
                buttons[combo[0]].getText().equals(buttons[combo[1]].getText()) &&
                buttons[combo[0]].getText().equals(buttons[combo[2]].getText())) {
                return true;
            }
        }
        return false;
    }

    private boolean isDraw() {
        for (JButton button : buttons) {
            if (button.getText().equals("")) {
                return false;
            }
        }
        return true;
    }

    private void disableAllButtons() {
        for (JButton button : buttons) {
            button.setEnabled(false);
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(TicTacToe::new);
    }
}
