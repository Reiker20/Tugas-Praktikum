pipeline {
    agent any
    
    environment {
        IMAGE_NAME = 'Reiker20/Tugas-Praktikum'
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
                echo "Mengunggah Docker Image ke Docker Hub azskiees..."
                withCredentials([usernamePassword(credentialsId: REGISTRY_CREDENTIALS, 
                    usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    
                    // Login ke Docker Hub menggunakan kredensial
                    bat 'docker login -u %USER% -p %PASS%'
                    bat "docker push %IMAGE_NAME%:%BUILD_NUMBER%"
                    
                    // Tag dan push image sebagai 'latest'
                    bat "docker tag %IMAGE_NAME%:%BUILD_NUMBER% %IMAGE_NAME%:latest"
                    bat "docker push %IMAGE_NAME%:latest"
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
