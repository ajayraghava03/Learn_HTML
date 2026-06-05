import java.applet.Applet;
import java.awt.*;
import java.util.*;

public class DigitalClockApplet extends Applet implements Runnable {
    Thread t;

    public void init() {
        t = new Thread(this);
        t.start();
    }

    public void run() {
        while (true) {
            repaint();
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {}
        }
    }

    public void paint(Graphics g) {
        Calendar cal = Calendar.getInstance();
        g.drawString(cal.getTime().toString(), 50, 50);
    }
}
