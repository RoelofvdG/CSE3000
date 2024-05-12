package nl.roelofvdg;

import org.junit.Test;

import static org.junit.Assert.assertEquals;


public class CalculatorTest {

    @Test
    public void add() {
        Calculator calc = new Calculator();
        assertEquals(calc.add(1, 2), 3);
    }
}