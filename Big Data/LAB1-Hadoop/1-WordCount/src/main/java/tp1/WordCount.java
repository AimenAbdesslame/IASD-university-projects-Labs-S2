package tp1;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class WordCount {

    public static void main(String[] args) throws Exception {
        // Hadoop passes class name as first argument, so we need args[1] and args[2]
        String inputPath;
        String outputPath;
        
        if (args.length == 2) {
            // Normal case: input and output only
            inputPath = args[0];
            outputPath = args[1];
        } else if (args.length == 3) {
            // Hadoop jar case: class name, input, output
            inputPath = args[1];
            outputPath = args[2];
        } else {
            System.err.println("Usage: WordCount <input path> <output path>");
            System.exit(-1);
            return;
        }
        
        System.out.println("Input path: " + inputPath);
        System.out.println("Output path: " + outputPath);
        
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "word count");
        
        job.setJarByClass(WordCount.class);
        job.setMapperClass(TokenizerMapper.class);
        job.setCombinerClass(IntSumReducer.class);
        job.setReducerClass(IntSumReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);
        
        FileInputFormat.addInputPath(job, new Path(inputPath));
        FileOutputFormat.setOutputPath(job, new Path(outputPath));
        
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
