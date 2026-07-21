static class Singleton {
    private static volatile Singleton s;
    private String value;

    private Singleton() {
        s = null;
        value = "";
    }

    public static Singleton getInstance() {
        if (s == null) {
            synchronized(Singleton.class) {
                s = new Singleton();
            }
        }
        return s;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        synchronized(Singleton.class) {
            this.value = value;
        }
    }
    
}
