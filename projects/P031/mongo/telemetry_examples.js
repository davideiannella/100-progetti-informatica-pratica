db.telemetry.createIndex({deviceId:1, ts:-1});
db.telemetry.insertOne({
  deviceId:"sensor-01",
  ts:new Date(),
  metrics:{temperature:22.4, humidity:51.0}
});
db.telemetry.find({deviceId:"sensor-01"}).sort({ts:-1}).limit(10);
