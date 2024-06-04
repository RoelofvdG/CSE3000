package nl.roelofvdg.templateit_5;

class NamedStyle
{
    private final String name;
    private final boolean hasParam;
    private int row;
    private int column;

    public NamedStyle(String name, boolean hasParam)
    {
        this.name = name;
        this.hasParam = hasParam;
    }

    public String getName()
    {
        return name;
    }

    public boolean hasParam()
    {
        return hasParam;
    }

    public int getRow()
    {
        return row;
    }

    public int getColumn()
    {
        return column;
    }

    public void setRow(int row)
    {
        this.row = row;
    }

    public void setColumn(int column)
    {
        this.column = column;
    }

    public String toString()
    {
        return "@style("+getName()+","+hasParam()+")";
    }
}

