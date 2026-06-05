import java.awt.*;
import java.awt.event.*;
import java.applet.Applet;

public class CurrencyConverterApplet extends Applet implements ActionListener {
    TextField inputField, resultField;
    Choice currencyChoice;
    Button convertButton;

    // Conversion rates
    double usdToEur = 0.85;
    double usdToGbp = 0.75;
    double usdToInr = 82.5;
    double usdToAud = 1.5;

    public void init() {
        // Layout and components
        setLayout(new GridLayout(5, 2, 5, 5));

        Label inputLabel = new Label("Enter amount in USD:");
        inputField = new TextField(10);

        Label currencyLabel = new Label("Select currency:");
        currencyChoice = new Choice();
        currencyChoice.add("EUR");
        currencyChoice.add("GBP");
        currencyChoice.add("INR");
        currencyChoice.add("AUD");

        convertButton = new Button("Convert");
        convertButton.addActionListener(this);

        Label resultLabel = new Label("Converted amount:");
        resultField = new TextField(10);
        resultField.setEditable(false);

        // Add components to applet
        add(inputLabel);
        add(inputField);
        add(currencyLabel);
        add(currencyChoice);
        add(new Label()); // Empty space
        add(convertButton);
        add(resultLabel);
        add(resultField);
    }

    public void actionPerformed(ActionEvent e) {
        try {
            double amountInUsd = Double.parseDouble(inputField.getText());
            double convertedAmount = 0.0;

            String selectedCurrency = currencyChoice.getSelectedItem();
            switch (selectedCurrency) {
                case "EUR":
                    convertedAmount = amountInUsd * usdToEur;
                    break;
                case "GBP":
                    convertedAmount = amountInUsd * usdToGbp;
                    break;
                case "INR":
                    convertedAmount = amountInUsd * usdToInr;
                    break;
                case "AUD":
                    convertedAmount = amountInUsd * usdToAud;
                    break;
            }

            resultField.setText(String.format("%.2f %s", convertedAmount, selectedCurrency));
        } catch (NumberFormatException ex) {
            resultField.setText("Invalid input");
        }
    }
}
