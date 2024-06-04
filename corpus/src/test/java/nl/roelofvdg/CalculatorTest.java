package nl.roelofvdg;

import org.junit.Test;

import static org.junit.Assert.assertEquals;
// INSERT IMPORTS HERE

public class CalculatorTest {

    @Test
    public void add() {
        Calculator calc = new Calculator();
        assertEquals(calc.add(1, 2), 3);
    }

    @Test
    public void testAdd() {
        Calculator calculator = new Calculator();
        assertEquals(calculator.add(1, 2), 3);
    }
}