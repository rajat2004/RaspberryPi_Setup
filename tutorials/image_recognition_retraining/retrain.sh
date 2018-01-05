link= ""

wget $link

tar -xvf pascal_voc

mkdir pascal_voc/bottlenecks

sudo python retrain.py \
    --image_dir pascal_voc\
    --bottleneck_dir=pascal_voc/bottlenecks\
    --learning_rate=0.0001 \
    --testing_percentage=20 \
    --validation_percentage=20 \
    --train_batch_size=32 \
    --validation_batch_size=-1 \
    --flip_left_right True \
    --random_scale=30 \
    --random_brightness=30 \
    --eval_step_interval=100 \
    --output_graph=mobilenet_1.0_224_retrained_graph.pb\
    --output_labels=mobilenet_1.0_224_retrained_labels.txt\
    --how_many_training_steps=10000 \
    --architecture mobilenet_1.0_224
