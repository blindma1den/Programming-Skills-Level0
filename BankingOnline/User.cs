


public class User
{
    public string Name { get; set; }
    public string Password { get; set; }
    public int Balance { get; set; }
    internal void DepositMoneyUser(int mount)
    {
        this.Balance += mount;
    }

    internal void WithDrawMoneyUser(int mount)
    {
        this.Balance -= mount;
    }
}