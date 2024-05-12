package nl.roelofvdg.jnfe_6;

public class AbstractNFeAdaptadorBean {
    /**
     * Calcula o d�gito verificador.
     *
     * @param chNFe
     */
    public static int calculaDV(String chNFe) {
        int soma = calculaSomaDV(chNFe);
        int dv = 11 - (soma % 11);
        dv = dv > 9 ? 0 : dv;
        return dv;
    }

    public static int calculaSomaDV(String chNFe) {
        if (chNFe.length() != 43) {
            throw new IllegalArgumentException(
                    "Comprimento da chave '"+chNFe+"' precisa ser 43, mas � "
                            + chNFe.length());
        }
        int soma = 0;
        for (int i = 0; i < 43; i++) {
            soma += Character.getNumericValue(chNFe.charAt(i))
                    * convertePosPeso(i + 1, 43);
        }
        return soma;
    }

    public static int convertePosPeso(int posicao, int comprimento) {
        return ((comprimento - posicao) % 8) + 2;
    }

}
