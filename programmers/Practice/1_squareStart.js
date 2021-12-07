process.stdin.setEncoding('utf8');
process.stdin.on('data', data => {
    const [n, k] = data.split(" ");
    for (let i=0; i < k; i++) {
        console.log('*'.repeat(n));        
    }
});