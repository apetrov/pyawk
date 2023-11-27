{
    for (i = 1; i <= NF; i++)
        word_count++;
}
END {
    print "Total word count: " word_count;
}
