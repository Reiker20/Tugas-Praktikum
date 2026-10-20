pipeline {
    agent any
    
    environment {
        // PERUBAHAN: Ubah nama repository menjadi huruf kecil semua
        IMAGE_NAME = 'reikaelvaretta/tugas-praktikum'
        REGISTRY_CREDENTIALS = 'dockerhub-credentials'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo "Berhasil mengambil kode dari GitHub."
            }
        }
        
        stage('Build Database & App') {
            steps {
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
                echo "Mengunggah Docker Image ke Docker Hub..."
                withCredentials([usernamePassword(credentialsId: REGISTRY_CREDENTIALS, 
                    usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    
                    bat 'docker login -u %USER% -p %PASS%'
                    bat "docker push %IMAGE_NAME%:%BUILD_NUMBER%"
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
            echo "Build dan Push Docker Image BERHASIL!"
        }
        failure {
            echo "Terjadi kesalahan saat menjalankan pipeline."
        }
    }
}
