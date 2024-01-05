package com.example.primerparcial.aed3.challenge_1_2;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    private EditText username, password;
    private DataBaseAdmin dataBaseAdmin;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        username = findViewById(R.id.username);
        password = findViewById(R.id.password);

        dataBaseAdmin = new DataBaseAdmin(this, "Admin", null, 1);

        SharedPreferences data = getSharedPreferences("data", Context.MODE_PRIVATE);
        SharedPreferences.Editor editor = data.edit();
        editor.putInt("tries", 0);
        editor.apply();
    }

    public void logIn(View view) {
        String user = username.getText().toString();
        String pass = password.getText().toString();

        if (user.isEmpty() || pass.isEmpty()) {
            Toast.makeText(this, "Complete los datos", Toast.LENGTH_SHORT).show();
        } else {
            if (!isUserBlocked()) {
                SQLiteDatabase db = dataBaseAdmin.getWritableDatabase();
                Cursor cursor = db.rawQuery("SELECT ID FROM USERS WHERE NAME=\"" + user + "\" AND PASSWORD=\"" + pass + "\"", null);

                if (cursor.moveToFirst()) {
                    Intent menu = new Intent(this, Menu.class);
                    menu.putExtra("user_id", cursor.getInt(0));
                    startActivity(menu);
                } else {
                    countTry();
                    Toast.makeText(this, "Datos Incorrectos", Toast.LENGTH_SHORT).show();
                }

                db.close();
            }
        }
    }

    private boolean isUserBlocked() {
        SharedPreferences data = getSharedPreferences("data", Context.MODE_PRIVATE);
        int tries = data.getInt("tries", 0);

        if (tries == 3) {
            Toast.makeText(this, "Usuario Bloqueado", Toast.LENGTH_SHORT).show();
            return true;
        }

        return false;
    }

    private void countTry() {
        SharedPreferences data = getSharedPreferences("data", Context.MODE_PRIVATE);
        int tries = data.getInt("tries", 0);
        SharedPreferences.Editor editor = data.edit();
        editor.putInt("tries", tries + 1);
        editor.apply();
    }
}