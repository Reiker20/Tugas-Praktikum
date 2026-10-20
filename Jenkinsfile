pipeline {
    agent any
    
    environment {
        // Menggunakan username Docker Hub: azskiees
        IMAGE_NAME = 'azskiees/tugas-komputasi-awan'
        // ID Kredensial yang didaftarkan di Manage Credentials Jenkins
        REGISTRY_CREDENTIALS = 'dockerhub-credentials'
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Mengambil kode sumber dari repositori GitHub
                checkout scm
                echo "Berhasil mengambil kode dari GitHub."
            }
        }
        
        stage('Build Database & App') {
            steps {
                // Menjalankan proses persiapan dan pengujian basis data
                echo "Mempersiapkan pengujian lingkungan aplikasi dan koneksi basis data..."
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Mulai proses build Docker Image..."
                bat "docker build -t %IMAGE_NAME%:%BUILD_NUMBER% ."
            }
        }
        
        stage('Push Docker Image') {
            steps {
                script {
                    // Autentikasi dan push image ke akun Docker Hub azskiees
                    echo "Mengunggah Docker Image ke Docker Hub azskiees..."
                    docker.withRegistry('https://index.docker.io/v1/', REGISTRY_CREDENTIALS) {
                        def tag = "${IMAGE_NAME}:${env.BUILD_NUMBER}"
                        // Push dengan tag sesuai nomor build (contoh: azskiees/tugas-komputasi-awan:1)
                        docker.image(tag).push()
                        // Push dengan tag latest (azskiees/tugas-komputasi-awan:latest)
                        docker.image(tag).push('latest')
                    }
                }
            }
        }
    }
    
    post {
        always {
            echo "Seluruh tahapan pipeline Jenkins telah selesai dieksekusi."
        }
        success {
            echo "Build dan Push Docker Image ke Docker Hub azskiees BERHASIL!"
        }
        failure {
            echo "Terjadi kesalahan saat menjalankan pipeline."
        }
    }
}
