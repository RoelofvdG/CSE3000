package nl.roelofvdg.jnfe_6;

import org.junit.Test;

import static org.junit.Assert.*;
// INSERT IMPORTS HERE

public class AbstractNFeAdaptadorBeanTest {
    @Test
    public void converte() {
        assertEquals(2, AbstractNFeAdaptadorBean.convertePosPeso(43, 43));
        assertEquals(3, AbstractNFeAdaptadorBean.convertePosPeso(42, 43));
        assertEquals(8, AbstractNFeAdaptadorBean.convertePosPeso(37, 43));
        assertEquals(9, AbstractNFeAdaptadorBean.convertePosPeso(36, 43));
        assertEquals(2, AbstractNFeAdaptadorBean.convertePosPeso(35, 43));
        assertEquals(3, AbstractNFeAdaptadorBean.convertePosPeso(34, 43));
        assertEquals(4, AbstractNFeAdaptadorBean.convertePosPeso(1, 43));
        assertEquals(6, AbstractNFeAdaptadorBean.convertePosPeso(7, 43));
        assertEquals(3, AbstractNFeAdaptadorBean.convertePosPeso(10, 43));
    }

    @Test
    public void soma() {
        String chNFe = "5206043300991100250655012000000780026730161";
        assertEquals(43, chNFe.length());
        assertEquals(644, AbstractNFeAdaptadorBean.calculaSomaDV(chNFe));
    }
    @Test
    public void calcula() {
        String chNFe = "5206043300991100250655012000000780026730161";
        assertEquals(5, AbstractNFeAdaptadorBean.calculaDV(chNFe));
    }

    // INSERT TESTS HERE
}