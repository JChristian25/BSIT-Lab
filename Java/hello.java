package Java;

import java.awt.*;

public class hello
{
    public void drawRed(Graphics g, String displayString)
    {
        g.setColor(Color.red);
        g.drawString(displayString, 100, 100);
    }

    public void drawBlue(Graphics g, String displayString)
    {
        g.setColor(Color.blue);
        g.drawString(displayString, 100, 100);
    }
}