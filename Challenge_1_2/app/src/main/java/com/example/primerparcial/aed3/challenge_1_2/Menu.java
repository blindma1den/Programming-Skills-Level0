package com.example.primerparcial.aed3.challenge_1_2;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

public class Menu extends AppCompatActivity {

    private TextView greeting, balance;
    private DataBaseAdmin dataBaseAdmin;

    @SuppressLint("DefaultLocale")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_menu);

        greeting = findViewById(R.id.greeting);
        balance = findViewById(R.id.balance);

        dataBaseAdmin = new DataBaseAdmin(this, "Admin", null, 1);

        fillData();
    }

    @Override
    protected void onResume() {
        super.onResume();
        fillData();
    }

    public void withdraw(View view) {
        Intent withdrawIntent = new Intent(this, Withdraw.class);
        Bundle bundle = getIntent().getExtras();
        withdrawIntent.putExtra("user_id", bundle.getInt("user_id"));
        startActivity(withdrawIntent);
    }

    public void deposit(View view) {
        Intent depositIntent = new Intent(this, Deposit.class);
        Bundle bundle = getIntent().getExtras();
        depositIntent.putExtra("user_id", bundle.getInt("user_id"));
        startActivity(depositIntent);
    }

    public void close(View view) {
        finish();
    }

    private void fillData() {
        Bundle bundle = getIntent().getExtras();

        String username = "";
        String balanceAmount = "";

        SQLiteDatabase db = dataBaseAdmin.getWritableDatabase();
        Cursor cursor = db.rawQuery("SELECT NAME, BALANCE FROM USERS WHERE ID=" + bundle.getInt("user_id"), null);

        if (cursor.moveToFirst()) {
            username = "Hola " + cursor.getString(0);
            balanceAmount = "Tu saldo es: $" + String.format("%.2f", cursor.getFloat(1));
        } else {
            Toast.makeText(this, "Error", Toast.LENGTH_SHORT).show();
        }

        db.close();

        greeting.setText(username);
        balance.setText(balanceAmount);
    }
}