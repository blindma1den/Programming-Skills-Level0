package com.example.primerparcial.aed3.challenge_1_2;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

import androidx.annotation.Nullable;

public class DataBaseAdmin extends SQLiteOpenHelper {
    public DataBaseAdmin(@Nullable Context context, @Nullable String name, @Nullable SQLiteDatabase.CursorFactory factory, int version) {
        super(context, name, factory, version);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL("CREATE TABLE USERS(ID INTEGER PRIMARY KEY, NAME TEXT, PASSWORD TEXT, BALANCE DECIMAL(10,2))");
        db.execSQL("INSERT INTO USERS(NAME, PASSWORD, BALANCE) VALUES(\"valeria\", \"123\", 2000)");
        db.execSQL("INSERT INTO USERS(NAME, PASSWORD, BALANCE) VALUES(\"kevin\", \"456\", 2000)");
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        db.execSQL("DROP TABLE IF EXISTS USERS");
        db.execSQL("CREATE TABLE USERS(ID INTEGER PRIMARY KEY, NAME TEXT, PASSWORD TEXT)");
    }
}
