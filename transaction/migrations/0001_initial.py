# Generated by Django 3.0.5 on 2020-05-19 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plan', '0001_initial'),
        ('company', '0003_auto_20200519_0359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchant_id', models.CharField(max_length=150)),
                ('reference_code', models.CharField(max_length=100)),
                ('transaction_state', models.CharField(max_length=100)),
                ('risk', models.FloatField()),
                ('pol_response_code', models.CharField(max_length=300)),
                ('reference_pol', models.CharField(max_length=300)),
                ('signature', models.CharField(max_length=300)),
                ('pol_payment_method', models.CharField(max_length=300)),
                ('pol_payment_method_type', models.IntegerField()),
                ('installments_number', models.IntegerField()),
                ('tx_value', models.IntegerField()),
                ('tx_tax', models.IntegerField()),
                ('processing_date', models.DateField()),
                ('currency', models.CharField(max_length=10)),
                ('cus', models.CharField(max_length=300)),
                ('pse_bank', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=300)),
                ('iap_response_code', models.CharField(max_length=70)),
                ('iap_payment_method', models.CharField(max_length=300)),
                ('iap_payment_method_type', models.CharField(max_length=300)),
                ('iap_transaction_state', models.CharField(max_length=40)),
                ('message', models.CharField(max_length=300)),
                ('authorization_code', models.CharField(max_length=20)),
                ('pse_cycle', models.IntegerField()),
                ('transaction_id', models.CharField(max_length=40)),
                ('trazability_code', models.CharField(max_length=70)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Company')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.Plan')),
            ],
        ),
        migrations.CreateModel(
            name='Cancel_Or_Refund_Req',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_id', models.CharField(max_length=100)),
                ('request_type', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=15)),
                ('message', models.CharField(max_length=100)),
                ('mihpayid', models.CharField(max_length=100)),
                ('bank_ref_num', models.CharField(blank=True, max_length=100, null=True)),
                ('amount', models.DecimalField(decimal_places=6, default=0, max_digits=19)),
                ('error_code', models.CharField(max_length=10)),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.Transaction')),
            ],
        ),
    ]
