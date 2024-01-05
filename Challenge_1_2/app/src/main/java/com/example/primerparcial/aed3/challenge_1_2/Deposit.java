package com.example.primerparcial.aed3.challenge_1_2;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.content.ContentValues;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class Deposit extends AppCompatActivity {

    private TextView balanceTxt;
    private EditText amount;
    private Float balance;
    private DataBaseAdmin dataBaseAdmin;
    private Bundle bundle;

    @SuppressLint({"MissingInflatedId", "DefaultLocale", "SetTextI18n"})
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_deposit);

        balanceTxt = findViewById(R.id.depositTxt);
        amount = findViewById(R.id.depositAmount);

        dataBaseAdmin = new DataBaseAdmin(this, "Admin", null, 1);
        bundle = getIntent().getExtras();

        SQLiteDatabase db = dataBaseAdmin.getWritableDatabase();
        Cursor cursor = db.rawQuery("SELECT BALANCE FROM USERS WHERE ID=" + bundle.getInt("user_id"), null);

        if (cursor.moveToFirst()) {
            balance = cursor.getFloat(0);
            balanceTxt.setText("Tu saldo es: $" + String.format("%.2f", balance));
        } else {
            Toast.makeText(this, "Error", Toast.LENGTH_SHORT).show();
        }

        db.close();
    }

    @SuppressLint({"SetTextI18n", "DefaultLocale"})
    public void depositAmount(View view) {
        Float amountToDeposit = Float.valueOf(amount.getText().toString());
        balance = balance + amountToDeposit;
        SQLiteDatabase db = dataBaseAdmin.getWritableDatabase();
        ContentValues values = new ContentValues();
        values.put("BALANCE", balance);
        db.update("USERS", values, "ID=" + bundle.getInt("user_id"), null);
        db.close();
        balanceTxt.setText("Tu saldo es: $" + String.format("%.2f", balance));
        Toast.makeText(this, "Depósito Exitoso", Toast.LENGTH_SHORT).show();
    }

    public void closeDepositActivity(View view) {
        finish();
    }
}