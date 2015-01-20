---
title: Android期末考资料
layout: post
tags:
  - android
---

Android期末机考资料。

**Activity跳转与返回**

    mButton.setOnClickListener(new View.OnClickListener() {//第一个Activity跳转到第二个
        public void onClick(View v) {
            Intent mIntent = new Intent(MyActivity.this, NewActivity.class);
            Bundle mBundle = new Bundle();
            String s = mEditText.getText().toString();
            mBundle.putString("info", s);
            mIntent.putExtras(mBundle);
            startActivityForResult(mIntent, 1);
        }
    });
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {//第一个Activity从第二个接收信息
        String s = data.getExtras().getString("result");
        mTextView.setText(s);
    }
    //第二个Activity从第一个获取信息
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_new);
    Bundle mBundle = this.getIntent().getExtras();
    String s = mBundle.getString("info");
    //第二个Activity向第一个发送信息
    Intent intent = new Intent();
    String s = mEditText.getText().toString();
    intent.putExtra("result", s);
    NewActivity.this.setResult(RESULT_OK, intent);
    NewActivity.this.finish();