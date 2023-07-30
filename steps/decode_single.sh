#!/usr/bin/env bash

# ... (other parts of the script)

if [ -d "$audio_path" ]; then
  # Bulk decoding: Decoding multiple audio files in the directory
  for file in "$audio_path"/*.wav; do
    audio_id=$(basename "$file" .wav)
    $cmd JOB=1:$nj $dir/log/decode_${audio_id}.JOB.log \
      utils/queue.pl --num-threads $num_threads gmm-latgen-faster$thread_string --max-active=$max_active \
      --beam=$beam --lattice-beam=$lattice_beam --acoustic-scale=$acwt --allow-partial=true \
      --word-symbol-table=$graphdir/words.txt $decode_extra_opts \
      $model $graphdir/HCLG.fst "$feats" "ark:|gzip -c > $dir/lat_${audio_id}.JOB.gz" || exit 1;
  done
else
  # Single audio decoding: Decoding only the provided audio file
  audio_id=$(basename "$audio_path" .wav)
  $cmd JOB=1:$nj $dir/log/decode_${audio_id}.JOB.log \
    gmm-latgen-faster$thread_string --max-active=$max_active \
    --beam=$beam --lattice-beam=$lattice_beam --acoustic-scale=$acwt --allow-partial=true \
    --word-symbol-table=$graphdir/words.txt $decode_extra_opts \
    $model $graphdir/HCLG.fst "$feats" "ark:|gzip -c > $dir/lat_${audio_id}.JOB.gz" || exit 1;
fi

# ... (rest of the script)

